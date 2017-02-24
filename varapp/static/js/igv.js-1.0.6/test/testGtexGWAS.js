function runGtexGWASUnitTests() {

    asyncTest("gtexGWAS query", function () {

        var chr = "chr1",
            //bpStart = 67655271,
            //bpEnd   = 67684468,
            //bpStart = 1,
            //bpEnd   = 1000000000000000,
            bpStart = 240045908,
            bpEnd   = 249168436,
            featureSource = new igv.FeatureSource({
                type: 'gtexGWAS',
                url: 'data/misc/GWAS_catalog_SNPs_Pval5E08_hg19_040115_subset.txt'
            });

        featureSource.getFeatures(chr, bpStart, bpEnd, function (features) {

            ok(features);
            equal(16, features.length);   // feature count. Determined by grepping file
            equal(chr, features[ 0 ].chr); // ensure features chromosome is specified chromosome

            start();
        }, undefined);

    });

    asyncTest("gtexGWAS all features", function () {

        var featureSource = new igv.FeatureSource({
                type: 'gtexGWAS',
                url: 'data/misc/GWAS_catalog_SNPs_Pval5E08_hg19_040115_subset.txt'
            });

        featureSource.allFeatures(function (features) {

            ok(features);
            equal(194, features.length);   // feature count. Determined by grepping file

            start();
        });

    });

/*
    asyncTest("BED track line", function () {

        var featureSource = new igv.FeatureSource({
            type: 'bed',
            url: 'data/bed/basic_feature_3_columns.bed'
        });

        featureSource.getHeader(function (header) {

            ok(header);
            equal(header.name, "Basic Features");
            equal(header.color, "255,0,0");
            start();
        });

    });

    asyncTest("BED query gzip", function () {

        var chr = "chr1",
            bpStart = 67655271,
            bpEnd   = 67684468,
            featureSource = new igv.FeatureSource({
                type: 'bed',
                url: 'data/bed/basic_feature_3_columns.bed.gz'
            });

        featureSource.getFeatures(chr, bpStart, bpEnd, function (features) {

            ok(features);
            equal(128, features.length);   // feature count. Determined by grepping file
            equal(chr, features[ 0 ].chr); // ensure features chromosome is specified chromosome

            start();
        }, undefined);

    });

    asyncTest("broadPeak parsing ", function () {

        var featureSource,
            chr,
            bpStart,
            bpEnd;

        featureSource = new igv.FeatureSource({
            type: 'broadPeak',
            url: "data/peak/test.broadPeak"
        });

        chr = "chr22";
        bpStart = 16847690;
        bpEnd = 20009819;
        featureSource.getFeatures(chr, bpStart, bpEnd, function (features) {

            var feature;

            ok(features);
            equal(features.length, 100);   // # of features over this region

            feature = features[0];
            equal(chr, feature.chr);

            equal(feature.start, 16847690);
            ok(feature.end > bpStart);
            equal(feature.signal, 5.141275);

            start();

        }, undefined);

    });
*/


}
