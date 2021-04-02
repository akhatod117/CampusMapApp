
$(function() {
var classDiv = $('#classes');
var i = $('#classes p').size() + 1;

$('#addClass').live('click', function() {
        $('<p><label for="classes">Class <input type="text" id="class' + i +'"size="20" name="class' + i +'" value="" placeholder="Building Name" /></label> <a href="#" id="remClass">Remove</a></p>').appendTo(classDiv);
        i++;
        return false;
});

$('#remClass').live('click', function() { 
        if( i > 2 ) {
                $(this).parents('p').remove();
                i--;
        }
        return false;
});
});
