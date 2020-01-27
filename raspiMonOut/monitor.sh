while (true) do
  output="$(xprintidle)"
  if [ "$output" -gt "60000" ] ; then
    sudo echo 1 > /sys/class/backlight/rpi_backlight/bl_power
  else
    sudo echo 0 > /sys/class/backlight/rpi_backlight/bl_power
  fi
  sleep 1
done
