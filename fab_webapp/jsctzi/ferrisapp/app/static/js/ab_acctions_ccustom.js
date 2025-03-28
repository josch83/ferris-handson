// This js work is based on:
// Copyright (c) 2014, Serge S. Koval and contributors. See AUTHORS
// for more details.
//

//------------------------------------------------------
// AdminActions holds methods to handle UI for actions
//------------------------------------------------------
var AdminActions = function(viewname) {

    var chkAllFlag = true;
    var multiple = false;
    var single = false;
    var action_name = '';
    var action_url = '';
    var action_confirmation = '';
    var row_checked_class = 'success';
    var view_name = viewname.toLowerCase();

    this.execute_multiple = function(name, confirmation) {
        multiple = true;
        action_name = name;
        action_confirmation = confirmation;
        var selected = $('input.action_check:checked').size();

        if (selected == 0) {
            ab_alert('No row selected');
            return false;
        }

        if (!!confirmation) {
            $('#modal-confirm').modal('show');
        }
        else {
            form_submit();
        }
    };

    this.execute_single = function(url, confirmation) {
        single = true;
        action_url = url;
        action_confirmation = confirmation;

        if (!!confirmation) {
                $('#modal-confirm').modal('show');
        }
        else {
            window.location.href = action_url;
        }
    };

    function form_submit() {
        // Update hidden form and submit it

            var activeTabs = $('div.tab-pane.active');
            var form = null;

            if (activeTabs.length > 0)
            {
                // find action form
                var form = $('#action_form', $(activeTabs[0]));
                /*
                for(i=0; i < forms.length; i++)
                {
                    if (forms[i].parendNode.outerHTML.search(view_name) > 0)
                    {
                        form = forms[i];
                        break;
                    }
                }
                */
                $('#action', $(form)).val(action_name);
                $('input.action_check', $(form)).remove();
                $('input.action_check:checked', $(activeTabs[0])).each(function() {
                    $(form).append($(this).clone());
                });
                
            }
            else
            {
               form = $('#action_form');
               $('#action', form).val(action_name);
            
               $('input.action_check', form).remove();
               $('input.action_check:checked').each(function() {   
                   form.append($(this).clone());
               });
            }

            form.submit();

            return false;
    }

    //----------------------------------------------------
    // Event for checkbox with class "action_check_all"
    // will check all checkboxes with class "action_check
    //----------------------------------------------------
    $('.action_check_all').click(function() {

        var activeTabs = $('div.tab-pane.active');

        if (activeTabs.length > 0)
        {
           $('.action_check', $(activeTabs[0])).prop('checked', chkAllFlag).trigger("change");
           chkAllFlag = !chkAllFlag;
        }
        else
        {
           $('.action_check').prop('checked', chkAllFlag).trigger("change");
           chkAllFlag = !chkAllFlag;
        }
    });

    //----------------------------------------------------
    // Event for checkbox with class "action_check"
    // will add class 'active' to row
    //----------------------------------------------------
    $('.action_check').change(function() {
        var thisClosest = $(this).closest('tr'),
        checked = this.checked;
        $(this).closest('tr').add(thisClosest )[checked ? 'addClass' : 'removeClass'](row_checked_class);
    });

    //------------------------------------------
    // Event for modal OK button click (confirm.html)
    // will submit form or redirect
    //------------------------------------------
    $('#modal-confirm-ok').on('click', function(e) {
        if (multiple) {
            form_submit();
        }
        if (single) {
            window.location.href = action_url;
        }
    });

    //------------------------------------------
    // Event for modal show (confirm.html)
    // will replace modal inside text (div class modal-text) with confirmation text
    //------------------------------------------
    $('#modal-confirm').on('show.bs.modal', function(e) {
        if (multiple || single) {
            $('.modal-text').html(action_confirmation);
        }
    });

};