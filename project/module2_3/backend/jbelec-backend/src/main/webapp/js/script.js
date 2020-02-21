/*-- jQuery --*/
/*-- Default Action --*/
$(document).ready(function() {
	var width = screen.width;
	if (width<=992) {
		$('.navbar').hide();
		$('#clustrmaps-div').hide();
	}
	$('#shichuan-photo img').height($('#shichuan-info').height()-10);
	if (width<=768) {
		$('#shichuan-photo').hide();
		$('#shichuan-info').removeClass('col-lg-7 col-md-6 col-sm-8 col-xs-6');
	}
});

$('.nav li').mouseover(function(event) {
	$(this).addClass('active');
});
$('.nav li').mouseout(function(event) {
	$(this).removeClass('active');
});
