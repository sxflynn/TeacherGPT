package com.flynn.schooldb.util;

public enum LetterGrade {
    A_PLUS (97, "A+"),
    A      (93, "A"),
    A_MINUS(90, "A-"),
    B_PLUS (87, "B+"),
    B      (83, "B"),
    B_MINUS(80, "B-"),
    C_PLUS (77, "C+"),
    C      (73, "C"),
    C_MINUS(70, "C-"),
    D_PLUS(67,"D+"),
    D (63, "D"),
    D_MINUS (60, "D-"),
    F      (0,  "F");

    private final int threshold;
    private final String letter;

    LetterGrade(int threshold, String letter) {
        this.threshold = threshold;
        this.letter = letter;
    }

    public static String toLetterGrade(int score) {
        for (LetterGrade grade : LetterGrade.values()) {
            if (score >= grade.threshold) {
                return grade.letter;
            }
        }
        return F.letter;
    }
}
