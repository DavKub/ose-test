// Open Cypress Test Runner with npx cypress open

describe("Login to dashboard and navigate throughout the app", () => {
    beforeEach(() => {
        cy.restoreLocalStorage();
    });
    
    afterEach(() => {
        cy.saveLocalStorage();
    })

    before("Fills out credentials", () => {
        cy.visit("/");
        // Get all credential input fields, fill them and check correct value
        cy.get('#mat-input-0').as('username')
        cy.get('@username').clear();
        cy.get('@username').type('eugen').should('have.value', 'eugen');
        
        cy.get('#mat-input-1').as('password')
        cy.get('@password').clear();
        cy.get('@password').type('nasec').should('have.value', 'nasec');
        
        cy.get('.mat-raised-button').click();        
    });


    it("Request for landing page /cars", () => {
        cy.url().should('include', 'cars')
    });

    it("Request for fuel card page", () => {
        cy.visit('/dashboard/fuel-cards');
        cy.url().should('include', 'fuel-cards')
    })

    it("Request for drive book page", () => {
        cy.visit('/dashboard/drive-book');
        cy.url().should('include', 'drive-book')
    })
})
