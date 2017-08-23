# Charmin-High CHMT36VA Notes/Documentation

This repository serves as a resource for various information about the Charmin-High CHMT36VA. Most of this is applicable to other devices (CHMT48VA/B) but I'm concentrating on the CHMT36VA.

## Why CHMT36VA ##

There is a variety of low-cost pick-n-place machines out there. I choose the Charmin High CHMT36VA for a few reasons:

* Up and Down camera (critical for 0.5mm TQFP placement).
* Uses external computer, so will be easier to modify database files directly.
* Software was sent to me ahead of time to view/test (other manufactures won't do this it seems).
* Supported a range of tape sizes.
* Supported IC trays.

I wanted this device specifically to make target boards for my UFO Board. This is a pretty idea circumstance for a low-cost pick n place.

## Vision Notes ##

The camera makes a bounding box around the object based on bright spots it seems (i.e., legs which reflect well). You must be careful you don't get light shining in the camera (for example, from a window).

## Part-Specific Notes ##

### IC Devices ###

The default height of 0.5mm (this is somehow related to how low the Z-axis goes when placing, so a higher number means the part is higher) didn't seem as reliable on TQFP placements. I changed this height to about 0.8 (for TQPF64) and it worked very well.

