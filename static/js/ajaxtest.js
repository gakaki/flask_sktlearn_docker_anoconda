$(function() {
    $('button').click(function() {
        var url      = "http://127.0.0.1:9999/data_sales_num";
            // url      = "http://192.168.2.126:9999/data_sales_num";
        var json_str = JSON.stringify({
				// "series":[[2017,1,1655],[2017,2,963],[2017,3,1468],[2017,4,1269],[2017,5,1690],[2017,6,1706],[2017,7,1589],[2017,8,1931],[2017,9,2094]],
                "series":[["2016","14365"],["2017","14365"]],
				"next_date":"2018"
        });
        $.ajax({
            url: url,
            method: "POST",
            data: {
                json:json_str
            },
            dataType: "json",
            beforeSend :function(){
				
            },
		    complete: function(xhr, textStatus) {
		      //called when complete
				console.log(xhr,textStatus);
		    },
		    success: function(data, textStatus, xhr) {
		      //called when successful
				console.log(data, textStatus, xhr);
		    },
		    error: function(xhr, textStatus, errorThrown) {
		      //called when there is an error
				console.log(xhr, textStatus, errorThrown);
				
		    }
        })
    });
});

