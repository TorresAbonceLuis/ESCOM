pluginManagement {
    repositories {
        google()
        mavenCentral()
        maven { url = uri("https://mvn.0110.be/releases") }
        gradlePluginPortal()
    }
    resolutionStrategy {
        eachPlugin {
            if (requested.id.id == "com.android.application") {
                useModule("com.android.tools.build:gradle:8.2.2") // Cambia a la versión compatible
            }
        }
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven { url = uri("https://mvn.0110.be/releases") } // Añade esta línea
    }
}

rootProject.name = "ProyectoParte2"
include(":app")