$("#send-message").click(function getContactEmail() {
    var toEmail = $("p[name=to-email]").val();
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').attr("value");
    var url = `/contact/send_message/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'to_email': toEmail};

    $.post(url, data)
     .done(function() {
         location.reload();
    });
})