#!/usr/bin/perl

$mbin="/usr/local/bin2" ;
$domain=`$mbin/get_domain_from_sites -pwd` ; chop $domain ;

$prog="$0" ; 
if ( $prog =~ /.*\/web\/(\S+)/ ) { $prog0 = $1 ; }

print "Content-type: text/html\n\n";
$debug ="TEST";
print "<HTML>\n";

print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=euc-jp\">\n";

print "<Head><Title> www.$domain </Title></Head>";
print "<BODY bgcolor=\"#FFFFFF\">" ;

print " http://www.$domain/$prog0 は サンプル cgi として正常動作しております。 \n" ;

print " <!--- こちらのメッセージが見える場合は cgi が動作しておりません。 管理画面で cgi を許可に設定ください。--> \n" ;
print " <!--- もちろんブラウザの ソースを見る� で ご覧なれるのは  この� メッセージが御覧になれるのは � 正常な動作です。�--> \n" ;


print "</PRE>\n" ;


print "</Body>";
print "</HTML>\n";


exit  ;

