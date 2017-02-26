var five = require("johnny-five");
var Edison = require("edison-io");
var board = new five.Board({
  io: new Edison()
});

board.on("ready", function() {
  var a = new five.Motor({
    controller: "GROVE_I2C_MOTOR_DRIVER",
    pin: "A",
  });

  var b = new five.Motor({
    controller: "GROVE_I2C_MOTOR_DRIVER",
    pin: "B",
  });
 
if (input == "w")
{
	a.fwd(65);
	b.fwd(65);
}
else if (input == "s")
{
	a.stop();
    b.stop();
}
else if (input == "l")
{
	a.stop();
    b.stop();
	a.rev(30);
	b.fwd(30);
}
else if (input == "r")
{
	a.stop();
    b.stop();
	a.fwd(30);
	b.rev(30);
}
else
{
	delta = parseInt("input")
	a.fwd(60+delta);
	b.fwd(60-delta);
}
});
