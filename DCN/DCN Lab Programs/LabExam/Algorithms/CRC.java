package crc;

import java.util.Scanner;

public class CRC{

    // Function to perform XOR operation between two binary strings
    public static String xor(String a, String b) {
        int maxLength = Math.max(a.length(), b.length());
        int x = Integer.parseInt(a, 2);
        int y = Integer.parseInt(b, 2);
        String result = Integer.toBinaryString(x ^ y);
        result = String.format("%" + maxLength + "s", result).replace(" ", "0");
        return result;
    }

    // Function to perform division in CRC calculation
    public static String divide(String dividend, String divisor) {
        int divisorLength = divisor.length();
        int dividendLength = dividend.length();

        while (dividendLength >= divisorLength) {
            String temp;
            if (dividend.charAt(0) == '1') {
                temp = xor(divisor, dividend.substring(0, divisorLength));
            } else {
                temp = xor("0", dividend.substring(0, divisorLength));
            }
            dividend = temp.substring(1) + dividend.substring(divisorLength);
            dividendLength -= 1;
        }
        return dividend;
    }

    // Function to generate the codeword using CRC
    public static String generate(String message, String generator) {
        int messageLength = message.length();
        int generatorLength = generator.length();

        // Append zeros to the message to create the dividend
        String dividend = String.format("%-" + (messageLength + generatorLength - 1) + "s", message).replace(' ', '0');
        String remainder = divide(dividend, generator);

        // Return the original message concatenated with the remainder (codeword)
        return message + remainder;
    }

    // Function to check if the received codeword is correct
    public static boolean checkCodeWord(String codeword, String generator) {
        String remainder = divide(codeword, generator);
        // If remainder is zero, the codeword is correct
        return Integer.parseInt(remainder) == 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Using CRC-CCITT");
        String generator = "10001000000100001"; // Generator polynomial for CRC-CCITT

        while (true) {
            System.out.println("1. Generate codeword");
            System.out.println("2. Check data");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter dataword: ");
                    String dataword = scanner.next();
                    System.out.println("Codeword: " + generate(dataword, generator));
                    break;
                case 2:
                    System.out.print("Enter codeword: ");
                    String codeword = scanner.next();
                    if (checkCodeWord(codeword, generator)) {
                        System.out.println("No Error");
                    } else {
                        System.out.println("Error");
                    }
                    break;
                default:
                    System.out.println("Invalid choice, please select 1 or 2.");
            }
        }
    }
}
