# Generated by Django 4.2.13 on 2024-05-23 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geomatics', '0006_cadasterlanduseandlandmanagement_publish_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartographyandgeovisualization',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='cartographyandgeovisualization',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='engineeringsurvey',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='engineeringsurvey',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='fundamentalsofsurveying',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='fundamentalsofsurveying',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='geodesyandgravityfield',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='geodesyandgravityfield',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='geographicinformationsystem',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='geographicinformationsystem',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='globalnavigationsatellitesystem',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='globalnavigationsatellitesystem',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='photogrammetryremotesensingandimageprocessing',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='photogrammetryremotesensingandimageprocessing',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='projectplanningdesignandimplementation',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='projectplanningdesignandimplementation',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='spatialdatamanagementsystemandspatialdatainfrastructure',
            name='correctOpt',
        ),
        migrations.RemoveField(
            model_name='spatialdatamanagementsystemandspatialdatainfrastructure',
            name='weight',
        ),
        migrations.DeleteModel(
            name='cadasterLanduseAndLandManagement',
        ),
        migrations.DeleteModel(
            name='cartographyAndGeoVisualization',
        ),
        migrations.DeleteModel(
            name='engineeringSurvey',
        ),
        migrations.DeleteModel(
            name='fundamentalsOfSurveying',
        ),
        migrations.DeleteModel(
            name='geodesyAndGravityField',
        ),
        migrations.DeleteModel(
            name='geographicInformationSystem',
        ),
        migrations.DeleteModel(
            name='GlobalNavigationSatelliteSystem',
        ),
        migrations.DeleteModel(
            name='photogrammetryRemoteSensingandImageProcessing',
        ),
        migrations.DeleteModel(
            name='projectPlanningDesignAndImplementation',
        ),
        migrations.DeleteModel(
            name='spatialDataManagementSystemAndSpatialDataInfrastructure',
        ),
    ]
