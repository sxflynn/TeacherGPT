package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.Staff;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.Set;

public interface StaffRepository extends JpaRepository<Staff, Long>  {

    @Query("SELECT s FROM Staff s WHERE s.email LIKE %:keyword% OR s.firstName LIKE %:keyword% OR s.lastName LIKE %:keyword%")
    Set<Staff> searchByKeyword(@Param("keyword") String keyword);

    Set<Staff> findByLastNameIgnoreCase(String lastName);

    Set<Staff> findByFirstNameIgnoreCase(String firstName);

    Set<Staff> findByMiddleNameIgnoreCase(String middleName);

    Set<Staff> findByEmailIgnoreCase(String email);

    Set<Staff> findByPositionContains(String position);

    Set<Staff> findByStaffGradeLevelsGradeLevelGradeLevelNameContainsIgnoreCase(String name);

}
