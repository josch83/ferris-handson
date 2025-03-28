//---------------------------------------
// Function for keeping tab focus
// after page reload, uses cookies
//---------------------------------------
$(function () {
    $('a[data-toggle="tab"]').on('shown.bs.tab', function () {
        localStorage.setItem('lastTab', $(this).attr('href'));
    });

    var lastTab = localStorage.getItem('lastTab');

    if (window.location.hash !== undefined && $('a[href="' + window.location.hash + '"').length > 0) {
        $('a[href="' + window.location.hash + '"').tab('show');
    }
    else if (lastTab) {
        $('a[href="' + lastTab + '"]').tab('show');
    } else {
        // Set the first tab if cookie do not exist
        $('a[data-toggle="tab"]').first().tab('show');
    }

});


