/*
 * jQuery TableFix plugin ver 1.0.1
 * Copyright (c) 2010 Otchy
 * This source file is subject to the MIT license.
 * http://www.otchy.net
 */
(function($){
	$.fn.tablefix = function(options) {
		return this.each(function(index){
			// 処理継続の判定
			var opts = $.extend({}, options);
			var baseTable = $(this);
			var withWidth = (opts.width > 0) && (opts.width - 20 < baseTable.width());
			var withHeight = (opts.height > 0) && (opts.height -20 < baseTable.height());
			if (!withWidth) {
				opts.width = baseTable.width() + 20;
			}
			if (!withHeight) {
				opts.height = baseTable.height() + 20;
			}
			if (!withWidth && !withHeight) {
				return;
			}
			// 外部 div の設定
			baseTable.wrap("<div></div>");
			var div = baseTable.parent();
			div.css({position: "relative"});
			// スクロール部オフセットの取得
			var fixRows = (opts.fixRows > 0 && withHeight) ? opts.fixRows : 0;
			var fixCols = (opts.fixCols > 0 && withWidth) ? opts.fixCols : 0;
			var offsetX = 0;
			var offsetY = 0;
			baseTable.find('tr').each(function(indexY) {
				$(this).find('td,th').each(function(indexX){
					if (indexY == fixRows && indexX == fixCols) {
						var cell = $(this);
						offsetX = cell.position().left;
						offsetY = cell.parent('tr').position().top;
						return false;
					}
				});
				if (indexY == fixRows) {
					return false;
				}
			});
			if (withHeight) {
				offsetY -= 2;
			}
			// テーブルの分割と初期化
			var crossTable = baseTable.wrap('<div></div>');
			var rowTable = baseTable.clone().removeAttr('id').wrap('<div></div>');
			var colTable = baseTable.clone().removeAttr('id').wrap('<div></div>');
			var bodyTable = baseTable.clone().removeAttr('id').wrap('<div></div>');
			var crossDiv = crossTable.parent().css({position: "absolute", overflow: "hidden"});
			var rowDiv = rowTable.parent().css({position: "absolute", overflow: "hidden"});
			var colDiv = colTable.parent().css({position: "absolute", overflow: "hidden"});
			var bodyDiv = bodyTable.parent().css({position: "absolute", overflow: "auto"});
			div.append(rowDiv).append(colDiv).append(bodyDiv);
			// クリップ領域の設定
			var bodyWidth = opts.width - offsetX;
			var bodyHeight = opts.height - offsetY;
			crossDiv.width(offsetX).height(offsetY);
			rowDiv
				.width(bodyWidth - (withHeight ? 18 : 0))
				.height(offsetY)
				.css({left: offsetX + 'px'});
			rowTable.css({
				marginLeft: -offsetX + 'px'
			});
			colDiv
				.width(offsetX)
				.height(bodyHeight - (withWidth ? 18 : 0))
				.css({top: offsetY + 'px'});
			colTable.css({
				marginTop: -offsetY + 'px'
			});
			bodyDiv
				.width(bodyWidth)
				.height(bodyHeight)
				.css({left: offsetX + 'px', top: offsetY + 'px'});
			bodyTable.css({
				marginLeft: -offsetX + 'px',
				marginTop: -offsetY + 'px'
			});
			// スクロール連動
			bodyDiv.scroll(function() {
				rowDiv.scrollLeft(bodyDiv.scrollLeft());
				if (colDiv.scrollTop()!=bodyDiv.scrollTop()){
					colDiv.scrollTop(bodyDiv.scrollTop());
				}
			});
			colDiv.scroll(function() {
				if (colDiv.scrollTop()!=bodyDiv.scrollTop()){
					bodyDiv.scrollTop(colDiv.scrollTop());
				}
			});
			// 外部 div の設定
			div.width(opts.width).height(opts.height);
			//cloneで作成した表のurl消去
			$(crossTable).find('a').removeAttr("href");
			$(rowTable).find('a').removeAttr("href");
			if (withHeight && !withWidth) {
				$(colTable).find('a').removeAttr("href");
			} else {
				$(bodyTable).find('a').removeAttr("href");
			}
		});
	}
})(jQuery);