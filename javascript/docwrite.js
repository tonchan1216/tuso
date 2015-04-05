/**
 * @author shunsuke
 */
 
function chgpimg(obj)
{
   url="images/p" + obj.id + ".png";
   document.getElementById(obj.id).src=url;
}

function chgimg(obj)
{
   url="images/" + obj.id + ".png";
   document.getElementById(obj.id).src=url;
}

// 読み込みに時差が発生するため、プレロード
(new Image()).src="images/lastconcert.png";
(new Image()).src="images/pastconcert.png";
(new Image()).src="images/introduction.png";
(new Image()).src="images/joinus.png";
(new Image()).src="images/contact.png";
(new Image()).src="images/link.png";
 
 
document.write("<a href='concert.html'     title='これからの演奏会のお知らせです'><img src='images/lastconcert.png' id='lastconcert' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu' alt='最新の演奏会' width='167' height='32' /></a><br />");
document.write("<a href='pastconcert.html' title='今まで演奏してきた曲目などです'><img src='images/pastconcert.png' id='pastconcert' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu' alt='過去の演奏会' width='167' height='32' /></a><br />");
document.write("<a href='profile.html'     title='活動方針などです'               ><img src='images/introduction.png' id='introduction' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu' alt='当団について' width='167' height='32' /></a><br />");
document.write("<a href='joinus.html'      title='募集パートなどです'             ><img src='images/joinus.png'  id='joinus' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu' alt='団員募集'    width='167' height='32' /></a><br />");
document.write("<a href='clipmail/clipmail.html'     title='お気軽にお問い合わせください' ><img src='images/contact.png'  id='contact' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu' alt='お問い合わせ' width='167' height='32' /></a><br />");
document.write("<a href='links.html'       title='お世話になっている方々です'     ><img src='images/link.png'  id='link' onmousedown=\"chgpimg(this)\" onmouseup=\"chgimg(this)\" class='menu'   alt='リンク'       width='167' height='32'  /></a><br />");