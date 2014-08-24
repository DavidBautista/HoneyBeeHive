{% load i18n %}
$(".add-worker-to-project .alert").html('<ul>{%if form.role.errors%}{% trans "Email" %}{{form.uworker.errors}}{%endif%}{%if form.role.errors%}{% trans "Role: "%}{{form.role.errors}}{% endif %}</ul>');
$(".add-worker-to-project .alert").show();
setTimeout(function(){$(".add-worker-to-project .alert").hide();}, 5000);
