#!/bin/bash


cond_to_letter() {
case $1 in
      Clear)
       echo a ;;
     Fair)
       echo b ;;
     ScatteredClouds)
       echo b ;;
     PartlyCloudy)
       echo c ;;
     ic)
       echo c ;;
     mc)
       echo d ;;
     c)
       echo e ;;
     MostlyCloudy)
       echo e ;;
     Overcast)
       echo f ;;
     LightRainShowers)
       echo h ;;
    ChanceOfRain)
       echo g ;;
     psus)
       echo g ;;
     ThunderstormAndrain)
       echo l ;;
     ChanceOfaThunderstorm)
       echo k ;;
     HeavyThunderstormsAndRain)
       echo n ;;
     Rain)
       echo i ;;
     LightSnow)
       echo p ;;
     mcfl)
       echo o ;;
     Thunderstorm)
       echo m ;;
     LightRain)
       echo s ;;
     LightDrizzle)
       echo s ;;
     i)
       echo E ;;
     sl)
       echo u ;;
     fr)
       echo i ;;
     Snow)
       echo p ;;
     SnowShowers)
       echo y ;;
     LightSnowShowers)
       echo y ;;
     w)
       echo 6 ;;
     ho)
       echo 5 ;;
     co)
       echo E ;;
     cl)
       echo A ;;
     mcl)
       echo B ;;
     mist)
       echo 9 ;;
     ShallowFog)
       echo 9 ;;
     Fog)
       echo 9 ;;
    esac
    }
     
cond=`conkyForecastWU -d CT $1 | tr -d ' '`
cond_to_letter $cond

