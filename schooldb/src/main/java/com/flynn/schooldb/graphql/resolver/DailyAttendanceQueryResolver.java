package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.service.DailyAttendanceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.time.LocalDate;
import java.util.List;

@Controller
public class DailyAttendanceQueryResolver {
    @Autowired
    private DailyAttendanceService dailyAttendanceService;

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentId(@Argument Long studentId) {
        return dailyAttendanceService.findByStudentStudentId(studentId);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByDate(@Argument LocalDate date) {
        return dailyAttendanceService.findByDate(date);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentIdAndDate(@Argument Long studentId, @Argument LocalDate date) {
        return dailyAttendanceService.findByStudentStudentIdAndDate(studentId, date);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByExcuseNoteNotNull() {
        return dailyAttendanceService.findByExcuseNoteNotNull();
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentIdAndAttendanceTypeName(@Argument Long studentId, @Argument String attendanceTypeName){
        return dailyAttendanceService.findByStudentStudentIdAndAttendanceTypeAttendanceType(studentId,attendanceTypeName);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByAttendanceTypeNameAndDate(@Argument String attendanceTypeName, @Argument LocalDate date){
        return dailyAttendanceService.findByAttendanceTypeAttendanceTypeAndDate(attendanceTypeName,date);
    }

    @QueryMapping
    public List<DailyAttendance> dailyAttendanceFindByStudentIdWhereNotFullAttendance(@Argument Long studentId){
        return dailyAttendanceService.findByStudentStudentIdAndNotFullAttendance(studentId);
    }
}



