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

print " http://www.$domain/$prog0 �� ����ץ� cgi �Ȥ�������ư��Ƥ���ޤ��� \n" ;

print " <!--- ������Υ�å���������������� cgi ��ư��Ƥ���ޤ��� �������̤� cgi ����Ĥ����꤯��������--> \n" ;
print " <!--- ������֥饦���� �������򸫤� �� �����ʤ��Τ�  ����� ��å������������ˤʤ��Τ� � �����ư��Ǥ����--> \n" ;


print "</PRE>\n" ;


print "</Body>";
print "</HTML>\n";


exit  ;

