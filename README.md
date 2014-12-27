Automate GUI control in Python.
============

## License and copyright ##
Autoaction is licensed under the GNU LGPL

## Example Code ##

	import os
	from autoaction import Autoaction
	
	if __name__ == "__main__":
	    file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
	    # Set the image directory
	    auto = Autoaction(file_dir)
	    # click_image() will click the image on the screen
	    # x, y is the width from the matching point.
	    auto.click_image("firefox_icon.png", x=5, y=5)
	    auto.sleep(3)
	    auto.click_image("search.png", x=5, y=5)
	    auto.sleep(1)
	    # type() will type the keyboard following the input string.
	    # When you input array string, you can use special keys.
	    auto.type(["python-autoaction", "<Enter>"])

