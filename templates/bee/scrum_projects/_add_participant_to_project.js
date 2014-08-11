var tr_wa = $("<tr>");
tr_wa.append($("<td>").text("{{awtp.uworker.name}}"));
tr_wa.append($("<td>").text("{{awtp.role}}"));
tr_wa.append($("<td>").text("{{awtp.get_permissions_display}}"));
$("#workers-assigned-table").append(tr_wa);