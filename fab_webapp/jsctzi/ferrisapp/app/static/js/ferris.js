$(document).ready(function () {
    $('a[href="' + window.location.pathname + '"]').addClass('curitem current')
    var pitem = $('a[href="' + window.location.pathname + '"]').parents("ul")
    pitem.attr("aria-expanded", true)
    pitem.siblings().attr("aria-expanded", true)
    pitem.parent('li').addClass('active current')
    pitem.addClass('in')

    //Tags module -> create tags from select2 box
    $(document).on('keyup', '.select2-container#s2id_tags > .select2-choices > .select2-search-field > input.select2-input', function (e) {
        var _this = $(this).parents(".select2-container#s2id_tags").siblings(".my_select2");
        if (e.keyCode === 13) {
            if ($(".select2-no-results").length >= 1) {
                var newval = $(this).val();
                $.ajax({
                    type: "POST",
                    url: "/api/v1/taxonomies/",
                    data: JSON.stringify({"name": newval}),
                    dataType: "json",
                    contentType: "application/json",
                    success: function (data) {
                        _this.append("<option value='" + data.id + "'>" + data.result.name + "</option>").trigger('change');

                        if (_this.val() == null) {
                            _this.val(data.id).trigger('change');
                        } else {
                            var oldval = _this.val();
                            oldval.push(data.id);
                            _this.val(oldval).trigger('change');
                        }
                    }
                });

            }
        }
    });

    $(document).on('change', '#generated-file-field[data-async]', function () {
        var _file_field = $('#generated-file-field')
        var file_data = _file_field[0].files[0];
        var form_data = new FormData();

        form_data.append('file', file_data);

        if (_file_field.data('bucket') !== undefined) {
            form_data.append('bucket', _file_field.data('bucket'))
        }

        $.ajax({
            url: '/files-storage/objects/upload',
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            type: 'post',
            success: function (data) {
                if ($("#generic-ajax-upload-holder")[0] === undefined) {
                    _file_field.after(
                        '<input type="hidden" id="generic-ajax-upload-holder" name="' + _file_field.attr('name') + '">'
                    );
                    _file_field.removeAttr("name");
                }
                console.log(data);
                $("#generic-ajax-upload-holder").val(data['file_name']);
            }
        });
    });

    $(document).ready(function() {
        console.log(document.location.pathname);
        if (document.location.pathname === "/esg/pre-execution/list/") {
            $("#list-add-btn").html('<i class="fa fa-plus"></i> Run');
        }
    });

});