## Web Experience Toolkit Drupal

This is a build profile for a Turnkey Linux appliance.  To build it, use [TKLDev](https://github.com/turnkeylinux-apps/tkldev) to generate an ISO that can be installed on VirtualBox or the virtualization environment of choice.

## Drupal WxT

The Drupal WxT distribution is a web content management system which assists in building and maintaining innovative Web sites that are accessible, usable, and interoperable. This distribution is open source software and free for use by departments and external Web communities.

Fundamentally this distribution relies and integrates extensively with the WET-BOEW jQuery Framework to leverage much of the accessibility support and extensively tested markup. Omega 4.x is used as the base theme for its exceptional HTML5 support and SASS / SMACSS based architecture. Where possible Drupal WxT will also pull work from the Panopoly and Spark Distributions due to the UX features and forward thinking design.

Development has been tailored for organizations that need to comply with standards for accessibility and bilingualism or that simply need a deployment based distribution that allows them to get up and running quickly using a carefully curated selection of modules that can support common enterprise business requirements. Specific information about how to work with this distribution can be found here: [Wiki Documentation](http://wiki.drupalwxt.org/)

## Benefits
* Provides reusable components for building and maintaining innovative Web sites.
* Respects accessibility [WCAG 2.0 AA](http://www.w3.org/TR/WCAG20/) and [WAI-ARIA](http://www.w3.org/TR/wai-aria/), usability, and interoperability
* Reduces costs by consolidating Web tools and solutions.
* Open source software that is free to use by departments and external Web communities.
* Responsive design (based on Omega) - mobile, tablet and desktop support
* Ever-growing list of open source plugins and widgets leverage through CTools Plugins.

## Credentials (passwords set at first boot)

Webmin, SSH, MySQL, phpMyAdmin: username root

Drupal 7: username admin

WARNING: When selecting a Drupal admin password, be sure to use one that meets the password policy for WET:

* Password must contain at least 3 characters of different types (lowercase, uppercase, digit or punctuation).
* Password must be at least 8 characters in length.
* Password must contain at least 2 letters.

If you are not able to login after first boot, you may not have selected an appropriate password.  You can reset it by connecting to the VM over SSH and typing:

`drush user-password admin --password=NEW_COMPLIANT_PASS`