var tr_wa = $("<tr>");
tr_wa.append($("<td>").text("{{awtp.uworker.name}}"));
tr_wa.append($("<td>").text("{{awtp.role}}"));
tr_wa.append($("<td>").text("{{awtp.permissions}}"));
$("#workers-assigned-table").append(tr_wa);