package com.flynn.schooldb.util;

import com.flynn.schooldb.dto.CourseGradeDTO;

import java.util.List;

public class GradeCalculator {
    /**
     * Calculate the average grade for a list of CourseGradeDTOs.
     *
     * @param allGradeSummaries List of CourseGradeDTO objects.
     * @return The average grade as a Float.
     */
    public static Float calculateGradeAverage(List<CourseGradeDTO> allGradeSummaries) {
        if (allGradeSummaries == null || allGradeSummaries.isEmpty()) {
            return 0f;
        }

        float localSum = 0f;
        int counter = 0;

        for (CourseGradeDTO courseGradeDTO : allGradeSummaries) {
            Float averageScore = courseGradeDTO.getAverageScoreFloat();
            if (averageScore != null) {
                localSum += averageScore;
                counter++;
            }
        }

        if (counter > 0) {
            return localSum / counter;
        } else {
            return 0f;
        }
    }


}
