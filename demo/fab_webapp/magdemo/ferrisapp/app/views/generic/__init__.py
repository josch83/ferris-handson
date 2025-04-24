import logging
from inspect import isclass

from ferrisapp.app.widgets import FerrisListWidget
from flask import url_for
from flask_appbuilder import BaseView, ModelView

from ...models.generic import FerrisGenericRelationshipType


class FerrisGenericModelView(ModelView):
    """
    Extended FAB ModelView
    - added one to one relationship support for related views (show or edit)
    - each related list widget now has search form
    """

    order_columns = [""]

    def _get_related_view_widget(
        self, item, related_view, order_column="", order_direction="", page=None, page_size=25
    ):
        """
        Overriden from Modelview. Added ONE_TO_ONE relationship support
        :param item:
        :param related_view:
        :param order_column:
        :param order_direction:
        :param page:
        :param page_size:
        :return:
        """

        fk = related_view.datamodel.get_related_fk(self.datamodel.obj)
        filters = related_view.datamodel.get_filters()

        if related_view.datamodel.is_relation_many_to_one(fk):
            filters.add_filter_related_view(
                fk,
                related_view.datamodel.FilterRelationOneToManyEqual,
                self.datamodel.get_pk_value(item),
            )
        elif related_view.datamodel.is_relation_many_to_many(fk):
            filters.add_filter_related_view(
                fk,
                self.datamodel.FilterRelationManyToManyEqual,
                self.datamodel.get_pk_value(item),
            )
        elif related_view.datamodel.is_relation_one_to_one(fk):
            filters.add_filter_related_view(
                fk,
                self.datamodel.FilterEqual,
                self.datamodel.get_pk_value(item),
            )
        else:
            if isclass(related_view) and issubclass(related_view, BaseView):
                name = related_view.__name__
            else:
                name = related_view.__class__.__name__

            return None

        widget = related_view._get_view_widget(
            filters=filters,
            order_column=order_column,
            order_direction=order_direction,
            page=page,
            page_size=page_size,
            relationship_type=related_view.datamodel.get_relationship_type(fk),
            foreign_key=self.datamodel.get_pk_value(item),
            foreign_key_value=self.datamodel.get_pk_value(item),
            read_only_fk=related_view.datamodel.is_read_only_fk(fk),
        )

        if isinstance(widget, FerrisListWidget):
            pass

        # print(f"Printing the latest widget where we need!!!! Are actions there?: {widget.template_args}", flush=True)

        return widget

    def _get_view_widget(self, **kwargs):
        """
        Added support for one-to-one relationship. This relationship can be represented with show or edit widget, controlled by `read_only_fk` kwarg
        Added search form to list widget

        :param relationship_type: one of FerrisGenericRelationshipTypes
        :param read_only_fk: applicable only to relationship_type == FerrisGenericRelationshipType.ONE_TO_ONE. If True related view will be rendered as show widget or edit widget if False
        :param foreign_key_value: value of foreign key

        :return widget
        """

        if kwargs.get("relationship_type", None) == FerrisGenericRelationshipType.ONE_TO_ONE:
            try:
                if not kwargs.get("read_only_fk", True):
                    return self._get_edit_widget(
                        form=self.edit_form.refresh(self.datamodel.get(kwargs.get("foreign_key_value"))),
                        pk=kwargs.get("foreign_key_value"),
                    ).get("edit")
                else:
                    item = self.datamodel.get(kwargs.get("foreign_key_value"))
                    return self._get_show_widget(pk=self.datamodel.get_pk_value(item), item=item).get("show")
            except Exception as e:
                logging.getLogger().error(e)

        widget = self._get_list_widget(**kwargs).get("list")
        # print(f"Actions in the view: {self.actions}", flush=True)
        # print(f"Printing the list view widget that shold contain actions: {widget}", flush=True)
        # print(f"Printing the content of the list view widget object as dict: {dir(widget)}", flush=True)
        # print(f"Printing the repr of the list view widget object: {repr(widget)}", flush=True)
        # print(f"Printing the template of the list view widget object: {widget.template}", flush=True)
        # print(f"Printing the template args of the list view widget object: {widget.template_args}", flush=True)

        setattr(
            widget,
            "show_search_widget",
            self._get_related_search_widget(
                form=self.search_form.refresh(),
                action=url_for(self.__class__.__name__ + ".list"),
                extra_id=self.__class__.__name__,
            ),
        )

        return widget

    def _get_edit_widget(self, form, exclude_cols=None, widgets=None, pk=None):
        """
        Added primary key to method arguments so edit widget can work in related view (or any other page)
        :param pk: id (primary key) of record that is rendered
        :return:
        """
        exclude_cols = exclude_cols or []
        widgets = widgets or {}
        widgets["edit"] = self.edit_widget(
            form=form,
            include_cols=self.edit_columns,
            exclude_cols=exclude_cols,
            fieldsets=self.edit_fieldsets,
            form_action=url_for(f"{self.__class__.__name__}.edit", pk=pk) if pk else None,
        )

        return widgets

    def _get_related_search_widget(self, form=None, exclude_cols=[], action="", extra_id=""):
        """
        Creating search widget with extra parameters passed to template so it can work properly when rendered as part of related list widget
        :param form: search form instance
        :param exclude_cols: columns to be excluded from search
        :param action: action url for form so it can work on right modelview
        :param extra_id: unique id for this widget needed for proper working of search filters
        :return:
        """
        widget = self.search_widget(
            route_base=self.route_base,
            form=form,
            include_cols=self.search_columns,
            exclude_cols=exclude_cols,
            filters=self._filters,
            action=action,
            extra_id=extra_id,
        )
        return widget
