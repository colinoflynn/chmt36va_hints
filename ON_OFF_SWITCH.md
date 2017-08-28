# Adding Saftey Switch #

The e-stop button is software-based, so I wanted something that I *KNEW* would kill the motors. Not so much for E-Stop purposes, but so I could reach into the machine safely without worry (i.e., when loading tapes), but without screwing up the communications protocol too badly that might happen if I switched the entire system off.

I wired in a DPDT switch to cut each of the power supplies to the stepper motor board.

When turning the switch back ON sometimes the motors shift a tiny bit, and you need to re-run the origin set task. This can easily be done by hitting the E-Stop button, which will pop up a window asking you to do this.

## Part Numbers ##

To wire the DPDT I used these parts:
* WM9127-ND to mate to the power supply connection.
* WM4999-ND (housing) + WM18820CT-ND (pins) to mate with the PCB.

To kill both boards you'll need 2x of each (+4x pins, recommend extra in case you screw up).

For the switch itself I used a fancy ABB switch which had a light in it so I could see if power was on or off. Note due to capacitors in driver boards it takes a bit for light to actually go off.

I also used a 28V LED (running at 36V, so will see how life is impacted), 350-2151-ND.