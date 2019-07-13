import '../scss/app.scss';

import $ from 'jquery';
import 'bootstrap';
import 'datatables.net';
import 'datatables.net-dt/css/jquery.dataTables.css';
import 'datatables.net-bs4';

$(document).ready( function () {

	let $form = $("form#search");
	let $search_input = $form.find('input#id_keyword');
	let $submit_btn = $form.find('input[type="submit"]');
	let data = [[1, "Example.com"]]
	let config = {
		"lengthChange": false,
		"info": false,
		"paging": false,
		"language": {
			"search": ""
		}
	}

	$form.submit(function (e) {
		e.preventDefault();
		let data = $form.serializeArray();
		console.log(data);
	});

	$search_input.keyup(function(){
	   if($(this).val() == ""){
			if ($('.alert-search').is(":hidden")) {
				$('.alert-search').show();
			};
		} else {
			$('.alert-search').hide();
		}
	 });

	$('table#top10').DataTable(config);
	$('table#keywords').DataTable(config);

} );
