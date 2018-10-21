use SampleDB

select Make, avg(MPG_City) as 'city miles' 
from cars 
group by Make


 
 select origin, sum(MSRP) as 'Total MSRP' 
 from cars
 Group by origin
 order by 'total MSRP' desc


 select DriveTrain, sum(weight) as 'Total Wieght'
 from cars
 group by DriveTrain


 select Origin ,type, count(Make) as 'number of cars'
 from cars
 group by Origin, type


 select Horsepower, count(make) as 'horsepower car count'
 from cars
 group by Horsepower
 order by 'horsepower car count' desc