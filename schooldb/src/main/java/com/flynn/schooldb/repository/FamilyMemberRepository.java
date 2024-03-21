package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.FamilyMember;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface FamilyMemberRepository extends JpaRepository<FamilyMember, Long> {

    @Query("SELECT f FROM FamilyMember f WHERE f.email LIKE %:keyword% OR f.firstName LIKE %:keyword% OR f.lastName LIKE %:keyword%")
    Set<FamilyMember> searchByKeyword(@Param("keyword") String keyword);

    Set<FamilyMember> findByLastNameIgnoreCase(String lastName);

    Set<FamilyMember> findByFirstNameIgnoreCase(String firstName);

    Set<FamilyMember> findByMiddleNameIgnoreCase(String middleName);

    Set<FamilyMember> findByPhoneNumberContains(String phoneNumber);


}
