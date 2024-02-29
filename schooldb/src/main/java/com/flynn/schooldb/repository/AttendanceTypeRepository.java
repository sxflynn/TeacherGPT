package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.AttendanceType;
import com.flynn.schooldb.entity.DailyAttendance;
import com.flynn.schooldb.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AttendanceTypeRepository extends JpaRepository<AttendanceType, Long> {

    List<AttendanceType> findAll();
}
