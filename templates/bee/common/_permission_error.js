var err = "Permission Denied";

// set the message to display: none to fade it in later.
var message = $('<div class="alert alert-danger errormessage" style="display: none;">');
// a close button
var close = $('<button type="button" class="close" data dismiss="alert">&times</button>');
message.append(close);
message.append(err);
message.appendTo($('body')).fadeIn(300).delay(3000).fadeOut(500);

