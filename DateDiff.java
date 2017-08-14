// Code snippet to calculate difference between two dates

import java.util.concurrent.TimeUnit;
import java.text.SimpleDateFormat;
import java.util.Calendar;
/*
  Not using Date/LocalDate classes as they are not supported by Android studio as yet.
*/

public int getDaysDiff(String yourDate){
  SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy");
  int date = 0;
  Calendar c = Calendar.getInstance();
  try {
      Long fromDate = simpleDateFormat.parse(""+yourDate).getTime();
      Long toDate = simpleDateFormat.parse(simpleDateFormat.format(c.getTime())).getTime();
      date = (int) TimeUnit.DAYS.convert(simpleDateFormat.parse(simpleDateFormat.format(c.getTime())).getTime()-simpleDateFormat.parse("28/05/1995").getTime(), TimeUnit.MILLISECONDS);
  }catch (Exception e){
      // log exception
  }
  return date;
}
