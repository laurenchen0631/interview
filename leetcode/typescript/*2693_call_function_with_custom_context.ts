declare global { 
    interface Function {
      callPolyfill(context: Record<any, any>, ...args: any[]): any;
	}
}

Function.prototype.callPolyfill = function(context: Record<any, any>, ...args): any {
    // Object.defineProperty(context, 'fn', {
    //     value: this,
    //     enumerable: false,
    // });

    // return context.fn(...args);
    return this.apply(context, args);
}
