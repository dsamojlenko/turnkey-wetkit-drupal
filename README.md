## Turnkey Wetkit Drupal

This is a build profile for a Turnkey Linux appliance.  To build it, use [TKLDev](https://github.com/turnkeylinux-apps/tkldev) to generate an ISO that can be installed on VirtualBox or the virtualization environment of choice.

## Drupal WxT

The [Drupal WxT distribution](https://github.com/wet-boew/wet-boew-drupal) is a web content management system which assists in building and maintaining innovative Web sites that are accessible, usable, and interoperable. This distribution is open source software and free for use by departments and external Web communities. This distribution relies and integrates extensively on the [WET-BOEW jQuery Framework](https://github.com/wet-boew) to leverage much of the rendering and overall markup.

Development has been tailored for organizations that need to comply with standards for accessibility and bilingualism or that simply need a distribution that allows them to get up and running quickly using a carefully curated selection of modules that can support common enterprise business requirements.

## Credentials (passwords set at first boot)

Webmin, SSH, MySQL, phpMyAdmin: username root

Drupal 7: username admin

WARNING: When selecting a Drupal admin password, be sure to use one that meets the password policy for WET:

* Password must contain at least 3 characters of different types (lowercase, uppercase, digit or punctuation).
* Password must be at least 8 characters in length.
* Password must contain at least 2 letters.

If you are not able to login after first boot, you may not have selected an appropriate password.  You can reset it by connecting to the VM over SSH and typing:

`drush user-password admin --password=NEW_COMPLIANT_PASS`