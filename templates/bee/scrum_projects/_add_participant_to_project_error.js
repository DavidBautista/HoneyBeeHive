{% load i18n %}
$(".add-worker-to-project .alert").html('<ul>{{form.uworker.errors}}{%if form.role.errors%}{% trans "role: "%}{{form.role.errors}}{% endif %}</ul>');
$(".add-worker-to-project .alert").show();
setTimeout(function(){$(".add-worker-to-project .alert").hide();}, 5000);
