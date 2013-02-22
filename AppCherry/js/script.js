(function($){
	$here 	= $('#here');
	$a		= $('a');
	$delay	= 720;
	$a.on('click', function(){
		if($here.is(':visible')) {
			$here.slideUp({duration:$delay, complete:function(){
				$a.text('Fun!');
			}});
		} else {
			$here.slideDown({duration:$delay, complete:function(){
				$a.text('click!');
			}});
		}
		
		return false;
	});
})(jQuery);