package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.GradeLevel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface GradeLevelRepository extends JpaRepository<GradeLevel, Long> {

    // All I need is findAll() which is inherited from JpaRepositry

}
