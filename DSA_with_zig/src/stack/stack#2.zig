const std = @import("std");

pub fn Stack(comptime T: type) type {
    return struct {
        const Self = @This();
        const Node = struct {
            value: T,
            next: ?*Node,
        };
        alloc: std.mem.Allocator = undefined,
        top: ?*Node = undefined,
        pub fn init(allocator: std.mem.Allocator) Self {
            return Self{ .alloc = allocator, .top = null };
        }
        pub fn deinit(self: *Self) void {
            while (self.pop()) |_| {}
        }
        pub fn push(self: *Self, v: T) !void {
            var newNode = try self.alloc.create(Node);
            newNode.value = v;
            newNode.next = self.top;
            self.top = newNode;
        }

        pub fn pop(self: *Self) ?T {
            var curr = self.top orelse return null;
            defer self.alloc.destroy(curr);
            self.top = curr.next;
            return curr.value;
        }

        pub fn peek(self: *Self) ?T {
            const node = self.top orelse return null;
            return node.value;
        }
        pub fn display(self: Self) void {
            var curr = self.top;
            while (curr) |node| : (curr = curr.next) {
                std.debug.print("{any} , ", .{node.value});
            }
        }
    };
}

test "stack functionalty" {
    var stack = Stack(i32).init(std.testing.allocator);
    defer stack.deinit();
    try stack.push(100);
    try std.testing.expect(stack.peek() == 100);
    try stack.push(200);
    try std.testing.expect(stack.peek() == 200);
    try std.testing.expect(stack.pop() == 200);
    try stack.push(300);
    try std.testing.expect(stack.pop() == 300);
}
