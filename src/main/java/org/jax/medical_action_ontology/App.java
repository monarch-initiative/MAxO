package org.jax.medical_action_ontology;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;


public class App 
{
    public static void main(String[] args) {

        Path indir = Paths.get("src/main/resources/Ontology_Terms/Most_Frequent_Sens");
        ArrayList<Thread> threads = new ArrayList<>();
        try (DirectoryStream<Path> files = Files.newDirectoryStream(indir)) {
            for (Path file : files) {
                Thread t = new Thread(new UMLSquery(file));
                t.setDaemon(false);
                threads.add(t);
            }
            /**
            for (Thread thread : threads) {
                thread.start();
            }
             **/
            //TODO: Fix-if run threads individually, no problem; if run all threads, some threads terminates before processing entire file.
           // threads.get(1).start(); //entire management
            threads.get(3).start();

        } catch (IOException E) {
            System.out.println("File opening error");
        }




    }


}
