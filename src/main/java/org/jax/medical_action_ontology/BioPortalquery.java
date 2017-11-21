package org.jax.medical_action_ontology;
import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.spi.mapper.JacksonMappingProvider;
import com.jayway.restassured.RestAssured;
import com.jayway.restassured.response.Response;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static com.jayway.restassured.RestAssured.given;


public class BioPortalquery {

    private static final String api_key = "7a8590b9-b311-48a8-8122-f913830c7599";
    static String outdir_path = "src/main/resources/Ontology_Terms/Most_Frequent_Sens_and_BioPortalxref/";

    public BioPortalquery() {
        Path outdir = Paths.get(outdir_path);
        try {
            Files.createFile(outdir);
        } catch (FileAlreadyExistsException e) {
            System.out.println("File already exist! \n Continue...");
        } catch (IOException e) {
            System.out.println("Incorrect file path!");
        }
    }

    public static void query(String term) {

        int pageNumber = 1;
        System.out.printf("Fetching result for page %d: \n", pageNumber);
        RestAssured.baseURI = "http://data.bioontology.org";
        Response response = given()
                .request().with()
                    .param("apikey", api_key)
                    .param("include", "prefLabel")
                    //.param("with_exact_match", true)
                    .param("page", pageNumber)
                    .param("pagesize", 5)
                    //.param("include_views", true) //unsure what it does
                    .param("include_views", false)
                    .param("display_context", false)
                    .param("display_links", false)
                    .param("ontology", "CHEBI")
                    .param("roots_only", true)
                .expect()
                    .statusCode(200)
                .get("search?q=" + term);

        String output = response.getBody().asString();

        System.out.println(output);
        Configuration config = Configuration.builder().mappingProvider(new JacksonMappingProvider()).build();
        BioPortalSearchResult[] results = JsonPath.using(config).parse(output).read("$.collection", BioPortalSearchResult[].class);

    }

    private class BioPortalSearchResult {
        private String prefLabel;
        private String id;
        private String type;

        public void setPrefLabel(String prefLabel) {
            this.prefLabel = prefLabel;
        }

        public String getPrefLabel() {
            return this.prefLabel;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getId() {
            return this.id;
        }

        public void setType(String type) {
            this.type = type;
        }

        public String getType() {
            return this.type;
        }
    }

    public static void main(String[] args) {
        query("valproic acid");
    }

}
