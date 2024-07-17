document.addEventListener('alpine:init', () => {
    Alpine.store('personas', {
        selected: "Persona 1",
        favicons: [
            {
                "id": "persona1",
                "url": "./icons/emma.svg",
                "name": "Emma, 82 Jahre alt",
                "description": "Emma ist eine verwitwete Rentnerin, die ihr ganzes Leben in einem kleinen Dorf verbracht hat. Ihre beiden Kinder leben weit entfernt und besuchen sie nur selten. Emma leidet unter leichter Demenz und Arthritis, was ihre Mobilität einschränkt. Sie benötigt emotionale Unterstützung und Hilfe bei alltäglichen Aufgaben wie Einkaufen und Hausarbeit. Da sie sich oft einsam fühlt, wünscht sie sich mehr soziale Kontakte. Die psychosoziale Betreuung umfasst regelmässige Besuche sowie die Begleitung zu lokalen Seniorengruppen und Mittagstischen."
            },
            {
                "id": "persona2",
                "url": "./icons/hans.svg",
                "name": "Hans, 76 Jahre alt",
                "description": "Hans ist ein ehemaliger Lehrer, der nach dem Tod seiner Frau vor zwei Jahren in eine tiefe Depression fiel. Er lebt allein in einer kleinen Wohnung in der Stadt und leidet zudem an Bluthochdruck. Hans braucht Unterstützung bei der Bewältigung seiner Trauer und bei der Pflege seines sozialen Netzwerks. Er hat großes Interesse an Literatur und würde gerne wieder an kulturellen Aktivitäten teilnehmen. Die Bedarfsabklärungsstelle hat Hans eine psychosoziale Begleitung zugesprochen. Diese hat zusammen mit Hans seine Interessen und Wünsche besprochen und verschiedene Optionen an seinem Wohnort geprüft. Am Anfang begleitet die Betreuungsperson Hans zu einer psychotherapeutischen Behandlung und zu einer Selbsthilfegruppe für Verwitwete. Die Selbsthilfegruppe organisiert vor allem gemeinsame Wanderungen, die Hans sehr geniesst. Hans braucht weniger blutdrucksenkende Medikamente. Zudem kann Hans einmal im Monat einen Lesezirkel besuchen und sich mit Gleichgesinnten über Literatur austauschen. Eine erneute Abklärung ein Jahr später hat gezeigt, dass Hans die Aktivitäten mittlerweile mehrheitlich selbstständig besuchen kann. Die psychosoziale Betreuungsperson kommt nur noch einmal im Monat vorbei um zu schauen, wie es Hans geht."
            },
            {
                "id": "persona3",
                "url": "./icons/marie.svg",
                "name": "Marie, 69 Jahre alt",
                "description": "Maria hat keine Familie mehr und lebt alleine in ihrer Wohnung. Früher war sie eine leidenschaftliche Gärtnerin. Sie möchte sich weiterhin nützlich fühlen und ihre Leidenschaft fürs Gärtnern ausüben. Dank der psychosozialen Begleitung konnte sie in ihrer Nähe ein Projekt zur solidari-schen Landwirtschaft ausfindig machen. Dort kann sie mit anderen Menschen sich ihrem Hobby widmen. Zudem führt sie mit ihrer Betreuungsperson regelmässig Ge-spräche, bei denen Sie mögliche Optionen für die Freizeitgestaltung besprechen. Sie fühlt sich wieder gebraucht und ist mittlerweile Mitglied im Organisationskomitee des solidarischen Landwirtschaftsprojektes."
            },
            {
                "id": "persona4",
                "url": "./icons/peter.svg",
                "name": "Peter, 74 Jahre alt",
                "description": "Peter ist geschieden und hat keinen Kontakt mehr zu seiner Familie. Seit Kurzem lebt er in einer Alterswohnung. Peter leidet an Diabetes. Er benötigt Hilfe bei der Verwaltung seiner Krankheit und bei der sozialen Integration in der neuen Wohnumgebung. Da er sich oft isoliert fühlt, hat er Schwierigkeiten, neue Freundschaften zu schliessen. Die psychosoziale Betreuung umfasst die Vermittlung und Begleitung zu sozialen Aktivitäten sowie eine regelmässige Gehbegleitung. Der psychsoziale Betreuer arbeitet dabei mit Pfleger*innen der Spitex zusammen und kann diese schnell auf gesundheitliche Verschlechterungen aufmerksam machen. Zudem beraten sie Peter gemeinsam in der Handhabung seiner Krankheit, sodass Peter mittlerweile einen sehr guten Umgang mit seiner Diabetes entwickeln konnte."
            },
            {
                "id": "Anna, 68 Jahre alt",
                "url": "./icons/anna.svg",
                "name": "Anna, 68 Jahre alt",
                "description": "Anna kam vor 50 Jahren aus Polen in die Schweiz und lebt seitdem in einer kleinen Wohnung in der Stadt. Sie ist verheiratet und gesundheitlich weitgehend stabil, leidet aber unter dem Gefühl der Isolation seitdem sie nicht mehr arbeitet. Anna fühlt sich oft zuhause eingeschlossen und fremd in der Schweiz, obwohl sie Deutsch spricht. Sie wünscht sich mehr Kontakte zu Menschen mit ähnlichem Hintergrund, um ihre kulturelle Identität zu pflegen und sich weniger isoliert zu fühlen. Dank regelmässigen Treffen mit anderen Migrant*innen sowie Begleitung zu kulturellen Veranstaltungen und Sprachcafés, fühlt sich Anna sozial und kulturell besser integriert."

            },
        ],
        selectPersona(name) {
            console.log("Vorher ausgewählt:", this.selected);
            this.selected = this.selected === name ? null : name;
            console.log("Nachher ausgewählt:", this.selected);
        },

        getSelectedName() {
            console.log("Aktuell ausgewählte Persona:", this.selected);
            const persona = this.favicons.find(favicon => favicon.name === this.selected);
            console.log("Gefundene Persona:", persona);
            return persona ? persona.name : '';
        },

        getSelectedDescription() {
            console.log("Aktuell ausgewählte Persona:", this.selected);
            const persona = this.favicons.find(favicon => favicon.name === this.selected);
            console.log("Gefundene Persona:", persona);
            return persona ? persona.description : '';
        }

    });
});

