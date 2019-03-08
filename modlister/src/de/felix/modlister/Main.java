package de.felix.modlister;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

/**
 * This is just a little script to make modlists
 *
 *  I know that this is not coded very well
 *
 * Created by felix on 7/12/2017.
 */
public class Main {
    public static void main (String[] args){
        File file = new File("mods/");
        try {
            write(file);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void write(File path) throws IOException {
        new File("disabledmodlist.txt").createNewFile();
        new File("modlist.txt").createNewFile();
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(new File("modlist.txt")));
        BufferedWriter disbledbufferedWriter = new BufferedWriter(new FileWriter(new File("disabledmodlist.txt")));
        File[] mods = path.listFiles();
        for (File file : mods){
            if (!file.isDirectory() && !file.getName().contains("lib") && !file.getName().endsWith(".disabled")) {
                bufferedWriter.write(file.getName().replace(".jar", "") + System.getProperty("line.separator"));
            }else if(file.getName().endsWith(".disabled")){
                disbledbufferedWriter.write(file.getName().replace(".jar.disabled", "") + System.getProperty("line.separator"));
            }
        }
        bufferedWriter.flush();
        bufferedWriter.close();
        disbledbufferedWriter.flush();
        disbledbufferedWriter.close();

    }
}
