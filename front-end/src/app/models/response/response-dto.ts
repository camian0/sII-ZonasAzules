export class ResposeDto{
    data: any;
    status: number;
    message: string;

    constructor() {
        this.data = "";
        this.status = 0;
        this.message = "";
    }
}