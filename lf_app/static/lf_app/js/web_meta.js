$("#btn_web_meta").click(
    function() {
        $.ajax({
            url: "/find_meta?url=" + $("#id_url").val(),

            success: function(result) {
                if(result.error) {
                    $("#lb_status").attr('class', 'alert alert-warning');
                    $("#lb_status").text('Failed to retrieve metadata: ' + result['error']);
                } else {
                    $("#id_title").val(result.title);
                    $("#id_tags").val(result.keywords);
                    $("#id_notes").val(result.description);

                    $("#lb_status").attr('class', 'alert alert-success');
                    $("#lb_status").text('Metadata retrieved successfully.');
                }
            },

            error: function(jqXHR, textStatus, errorThrown) {
                $("#lb_status").attr('class', 'alert alert-warning');
                $("#lb_status").text('Failed to retrieve metadata.');
            }
        });

        $("#lb_status").attr('class', 'alert alert-info');
        $("#lb_status").text('Retrieving metadata...');
    }
);
