$(document).ready(function () {
    $.fn.extend({
        popup:function(content,position){
            $(this).popover({
                trigger:'manual',
                placement:position,
                content:content,
            });
            $(this).popover('show');
            var that = this;
            setTimeout(function(){
                $(that).popover('destroy');
            },2000);
        }
    });
});
$.warning = function(message){
    $("#header-warning").html("<div class=\"alert alert-warning alert-dismissible fade in\" role=\"alert\" style=\"height: 50px;text-align:center;margin-bottom: 0px;\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">×</span></button><strong>"+message+"</strong></div>")
}
$.modal = function(tittle,message){
    if(tittle){
        $("#default-modal-tittle").html(tittle);
    }
    if(message){
        $("#default-modal-content").html(message);
    }
    $("#default-modal").modal();
}
