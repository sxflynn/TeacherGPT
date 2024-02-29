package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.AttendanceType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AttendanceTypeRepository extends JpaRepository<AttendanceType, Long> {

    List<AttendanceType> findAll();
}
