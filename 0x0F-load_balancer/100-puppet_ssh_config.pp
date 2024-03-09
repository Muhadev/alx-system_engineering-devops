#!/usr/bin/env bash
# setting up client config file
include stdlib

file { 'etc/ssh/ssh_config':
	ensure  => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	passwordAuthentication no
	",
}
