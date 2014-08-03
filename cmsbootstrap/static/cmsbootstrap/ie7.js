/* Use this script if you need to support IE 7 and IE 6. */

window.onload = function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'inasp-iconset\'">' + entity + '</span>' + html;
	}
	var icons = {
			'icon-twitter' : '&#xe000;',
			'icon-tick' : '&#xe001;',
			'icon-target' : '&#xe002;',
			'icon-star' : '&#xe003;',
			'icon-rss' : '&#xe004;',
			'icon-resource' : '&#xe005;',
			'icon-report' : '&#xe006;',
			'icon-publisher' : '&#xe007;',
			'icon-publication' : '&#xe008;',
			'icon-power-button' : '&#xe009;',
			'icon-person' : '&#xe00a;',
			'icon-home' : '&#xe00b;',
			'icon-gear' : '&#xe00c;',
			'icon-flag' : '&#xe00d;',
			'icon-event' : '&#xe00e;',
			'icon-e-resource' : '&#xe00f;',
			'icon-download' : '&#xe010;',
			'icon-document' : '&#xe011;',
			'icon-comment' : '&#xe012;',
			'icon-box' : '&#xe013;',
			'icon-book' : '&#xe014;',
			'icon-people' : '&#xe015;',
			'icon-pencil-paper' : '&#xe016;',
			'icon-network' : '&#xe017;',
			'icon-mail' : '&#xe018;',
			'icon-lock' : '&#xe019;',
			'icon-links' : '&#xe01a;',
			'icon-leaves' : '&#xe01b;',
			'icon-institution' : '&#xe01c;'
		},
		els = document.getElementsByTagName('*'),
		i, attr, html, c, el;
	for (i = 0; i < els.length; i += 1) {
		el = els[i];
		attr = el.getAttribute('data-icon');
		if (attr) {
			addIcon(el, attr);
		}
		c = el.className;
		c = c.match(/icon-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
};