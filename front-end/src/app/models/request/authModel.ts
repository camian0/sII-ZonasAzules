export class AuthModelRequest {
    email: string;
    password: string;
    role_id: number;

    constructor() {
        this.email = "";
        this.password = "";
        this.role_id = 2;
    }
}