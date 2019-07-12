import '../scss/app.scss';

import $ from 'jquery';
import 'bootstrap';
import 'datatables.net';
import 'datatables.net-dt/css/jquery.dataTables.css';
import 'datatables.net-bs4';


let data = [
	[1, "Example.com"]
]

$(document).ready( function () {

	let $form = $("form#search");
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

	$('table#top10').DataTable(config);
	$('table#keywords').DataTable(config);
} );
